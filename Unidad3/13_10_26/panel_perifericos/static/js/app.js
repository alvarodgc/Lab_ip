async function cargarConfuiguracion() {
    const respuesta= await fetch("/api/config");

    if (!respuesta.ok) {
        throw new Error("No se poede cargar");
    }

    const datos= await respuesta.json();
    document.querySelector("#titulo")
    .textContent= datos.titulo;
}
cargarConfiguracon();
