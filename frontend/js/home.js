(async function () {
  const featured = document.getElementById("featured");
  try {
    const products = await apiGet("/products");
    products.slice(0, 6).forEach(p => {
      const div = document.createElement("div");
      div.className = "card";
      div.innerHTML = `
        <img src="${p.image_url || "https://via.placeholder.com/300x200"}" alt="${p.name}">
        <h3>${p.name}</h3>
        <div class="row">
          <div class="muted">$${Number(p.price).toFixed(2)}</div>
          <a class="btn" href="product.html?id=${encodeURIComponent(p.id)}">Details</a>
        </div>
      `;
      featured.appendChild(div);
    });
  } catch (e) {
    featured.innerHTML = `<div class="notice warn">Failed to load products: ${e.message}</div>`;
  }
})();
