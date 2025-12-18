function renderStatus() {
  const status = new URLSearchParams(window.location.search).get("status");
  const el = document.getElementById("status");
  if (!status) return;

  if (status === "success") {
    el.innerHTML = `<div class="notice success">✅ Payment successful (test mode). Thank you!</div>`;
    // Optional: clear cart after success
    setCart([]);
  } else if (status === "cancel") {
    el.innerHTML = `<div class="notice warn">⚠️ Payment cancelled.</div>`;
  }
}

function renderCart() {
  const cart = getCart();
  const div = document.getElementById("cart");
  div.innerHTML = "";

  if (cart.length === 0) {
    div.innerHTML = `<div class="muted">Cart is empty. Go to <a href="products.html">Products</a>.</div>`;
    document.getElementById("total").innerText = "0.00";
    return;
  }

  cart.forEach(i => {
    const row = document.createElement("div");
    row.className = "row";
    row.style.margin = "8px 0";
    row.innerHTML = `
      <div>
        <b>${i.name}</b>
        <div class="muted">$${Number(i.price).toFixed(2)} × ${i.quantity}</div>
      </div>
      <button class="btn danger">Remove</button>
    `;
    row.querySelector("button").addEventListener("click", () => {
      removeCartItem(i.product_id);
      renderCart();
    });
    div.appendChild(row);
  });

  document.getElementById("total").innerText = cartTotal().toFixed(2);
}

async function checkout() {
  const items = getCart();
  if (!items.length) {
    alert("Cart is empty");
    return;
  }

  // Stripe session expects name/price/quantity
  const payload = { items: items, currency: "USD" };

  try {
    const res = await apiPost("/checkout", payload);
    window.location.href = res.checkout_url;
  } catch (e) {
    alert(`Checkout failed: ${e.message}`);
  }
}

renderStatus();
renderCart();
document.getElementById("checkoutBtn").addEventListener("click", checkout);
