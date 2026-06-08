/* Admin Dashboard JS — Digital Marketing Agency */
document.addEventListener('DOMContentLoaded', () => {
  // Sidebar active state
  const current = window.location.pathname.split('/').pop();
  document.querySelectorAll('.sidebar a').forEach(a => {
    if (a.getAttribute('href') === current) a.classList.add('active');
  });
});
