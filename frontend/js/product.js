(async function () {
  const detail = document.getElementById("detail");
  const id = new URLSearchParams(window.location.search).get("id");
  if (!id) {
    detail.innerHTML = `<div class="notice warn">Missing product id</div>`;
    return;
  }

  try {
    const p = await apiGet(`/products/${encodeURIComponent(id)}`);
    detail.innerHTML = `
      <img src="${p.image_url || "https://via.placeholder.com/700x300"}" alt="${p.name}">
      <h2 style="margin:12px 0 6px;">${p.name}</h2>
      <p class="muted" style="margin:0 0 10px;">$${Number(p.price).toFixed(2)}</p>
      <p class="muted">${p.description || "No description provided."}</p>
      <div class="row" style="margin-top:12px;">
        <button class="btn" id="add">Add to Cart</button>
        <a class="btn" href="cart.html">Go to Cart</a>
      </div>
    `;

    document.getElementById("add").addEventListener("click", () => {
      upsertCartItem({ product_id: p.id, name: p.name, price: Number(p.price), quantity: 1 });
      alert("Added to cart");
    });
  } catch (e) {
    detail.innerHTML = `<div class="notice warn">Failed to load product: ${e.message}</div>`;
  }
})();
