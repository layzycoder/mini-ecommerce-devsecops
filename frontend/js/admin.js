const API_BASE = "http://127.0.0.1:8000";

function setMsg(html) {
  document.getElementById("adminMsg").innerHTML = html || "";
}

async function loadOrders() {
  const password = document.getElementById("password").value;
  setMsg("");

  if (!password) {
    setMsg(`<div class="notice warn">Enter admin password.</div>`);
    return;
  }

  const res = await fetch(`${API_BASE}/orders`, {
    headers: { "X-Admin-Password": password }
  });

  if (res.status === 401) {
    setMsg(`<div class="notice warn">Unauthorized. Check password.</div>`);
    return;
  }
  if (!res.ok) {
    setMsg(`<div class="notice warn">Failed: HTTP ${res.status}</div>`);
    return;
  }

  const orders = await res.json();
  const table = document.getElementById("ordersTable");
  const body = document.getElementById("ordersBody");
  body.innerHTML = "";

  orders.forEach(o => {
    const itemsText = (o.items || []).map(i => `${i.name} × ${i.quantity}`).join(", ");
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${o.id || ""}</td>
      <td>${o.created_at || ""}</td>
      <td>${o.currency || ""}</td>
      <td>$${Number(o.total_amount || 0).toFixed(2)}</td>
      <td>${itemsText}</td>
    `;
    body.appendChild(tr);
  });

  table.style.display = "table";
}

document.getElementById("loadBtn").addEventListener("click", loadOrders);
