const API_BASE = window.location.origin;

async function apiGet(path) {
  const res = await fetch(`${API_BASE}${path}`);
  if (!res.ok) throw new Error(`GET ${path} failed: ${res.status}`);
  return res.json();
}

async function apiPost(path, body) {
  const res = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(data.detail || `POST ${path} failed: ${res.status}`);
  return data;
}

function getCart() {
  return JSON.parse(localStorage.getItem("cart") || "[]");
}
function setCart(cart) {
  localStorage.setItem("cart", JSON.stringify(cart));
}
function upsertCartItem(item) {
  const cart = getCart();
  const idx = cart.findIndex(x => x.product_id === item.product_id);
  if (idx >= 0) cart[idx].quantity += item.quantity;
  else cart.push(item);
  setCart(cart);
}
function removeCartItem(product_id) {
  const cart = getCart().filter(x => x.product_id !== product_id);
  setCart(cart);
}
function cartTotal() {
  return getCart().reduce((sum, i) => sum + (i.price * i.quantity), 0);
}
