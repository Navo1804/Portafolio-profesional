
// Galería de proyectos: switch de imagen principal al hacer clic en thumbnail
function switchImg(thumb) {
    const main = document.getElementById('gallery-main');
    if (!main) return;

    // Cambiar imagen principal
    main.src = thumb.src;
    main.alt = thumb.alt;

    // Actualizar estado activo
    document.querySelectorAll('.gallery-thumb').forEach(t => t.classList.remove('active'));
    thumb.classList.add('active');
}