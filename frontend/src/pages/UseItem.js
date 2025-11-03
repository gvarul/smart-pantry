import React, {useState, useEffect} from "react";
import { api } from "../api";

export default function UseItem(){
  const [items, setItems] = useState([]);
  const [selected, setSelected] = useState(null);
  const [qty, setQty] = useState(1);

  useEffect(()=>{ api.get("/items/user/1").then(r=>setItems(r.data)).catch(()=>{}); }, []);

  const useIt = async () => {
    try{
      await api.post("/usage/", { item_id: selected, used_quantity: qty });
      alert("Logged usage");
    } catch(e){ console.error(e); alert("Error");}
  };

  return (
    <div>
      <h2>Use Item</h2>
      <select onChange={e=>setSelected(parseInt(e.target.value))}>
        <option value="">-- select --</option>
        {items.map(i=> <option key={i.id} value={i.id}>{i.name} ({i.quantity} {i.unit})</option>)}
      </select>
      <br/>
      <label>Qty used: <input type="number" value={qty} onChange={e=>setQty(parseFloat(e.target.value))} /></label>
      <br/>
      <button onClick={useIt}>Use</button>
    </div>
  )
}
