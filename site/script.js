document.addEventListener('DOMContentLoaded', () => {
  const navItems = document.querySelectorAll('.nav-item[data-section]');
  const sections = document.querySelectorAll('.section');
  const topbarTitle = document.getElementById('topbar-title');
  const hamburger = document.getElementById('hamburger');
  const sidebar = document.querySelector('.sidebar');
  const overlay = document.querySelector('.overlay');
  const searchInput = document.getElementById('search-input');

  function showSection(id) {
    sections.forEach(s => s.classList.remove('active'));
    navItems.forEach(n => n.classList.remove('active'));
    const sec = document.getElementById(id);
    if (sec) {
      sec.classList.add('active');
      window.scrollTo({ top: 0 });
    }
    navItems.forEach(n => {
      if (n.dataset.section === id) {
        n.classList.add('active');
        topbarTitle.textContent = n.querySelector('.label')?.textContent || 'МАНУАЛЫ';
      }
    });
    sidebar.classList.remove('open');
    overlay.classList.remove('open');
  }

  navItems.forEach(item => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      showSection(item.dataset.section);
    });
  });

  // Quick nav cards
  document.querySelectorAll('.quick-card[data-go]').forEach(card => {
    card.addEventListener('click', () => showSection(card.dataset.go));
  });

  // Mobile
  hamburger?.addEventListener('click', () => {
    sidebar.classList.toggle('open');
    overlay.classList.toggle('open');
  });
  overlay?.addEventListener('click', () => {
    sidebar.classList.remove('open');
    overlay.classList.remove('open');
  });

  // Search
  searchInput?.addEventListener('input', (e) => {
    const q = e.target.value.toLowerCase().trim();
    if (!q) return;
    // Find section containing the query
    sections.forEach(sec => {
      if (sec.textContent.toLowerCase().includes(q)) {
        showSection(sec.id);
        // Highlight cards
        sec.querySelectorAll('.card').forEach(card => {
          if (card.textContent.toLowerCase().includes(q)) {
            card.style.borderColor = 'var(--accent)';
            card.scrollIntoView({ behavior: 'smooth', block: 'center' });
          } else {
            card.style.borderColor = '';
          }
        });
      }
    });
  });

  // Default section
  showSection('home');
});
