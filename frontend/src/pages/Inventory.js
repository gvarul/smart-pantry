import React, {useEffect, useState} from "react";
import { api } from "../api";

export default function Inventory(){
  const [items, setItems] = useState([]);
  useEffect(()=>{ api.get("/items/user/1").then(r=>setItems(r.data)).catch(()=>{}); }, []);
  return (
    <div>
      <h2>Inventory</h2>
      <table>
        <thead><tr><th>Name</th><th>Qty</th><th>Unit</th><th>Expiry</th></tr></thead>
        <tbody>
          {items.map(i=>(
            <tr key={i.id}><td>{i.name}</td><td>{i.quantity}</td><td>{i.unit}</td><td>{i.expiry_date}</td></tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}
