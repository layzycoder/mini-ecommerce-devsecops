(async function () {
  const container = document.getElementById("products");
  try {
    const products = await apiGet("/products");
    products.forEach(p => {
      const div = document.createElement("div");
      div.className = "card";
      div.innerHTML = `
        <img src="${p.image_url || "https://via.placeholder.com/300x200"}" alt="${p.name}">
        <h3>${p.name}</h3>
        <p class="muted">$${Number(p.price).toFixed(2)}</p>
        <div class="row">
          <a class="btn" href="product.html?id=${encodeURIComponent(p.id)}">View Details</a>
          <button class="btn" data-id="${p.id}">Add to Cart</button>
        </div>
      `;
      div.querySelector("button").addEventListener("click", () => {
        upsertCartItem({ product_id: p.id, name: p.name, price: Number(p.price), quantity: 1 });
        alert("Added to cart");
      });
      container.appendChild(div);
    });
  } catch (e) {
    container.innerHTML = `<div class="notice warn">Failed to load products: ${e.message}</div>`;
  }
})();
