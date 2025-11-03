import React, {useEffect, useState} from "react";
import { api } from "../api";

export default function ShoppingList(){
  const [list, setList] = useState([]);
  useEffect(()=>{ api.get("/shopping/user/1").then(r=>setList(r.data)).catch(()=>{}); }, []);
  const mark = async (id) => {
    await api.post(`/shopping/mark_purchased/${id}`);
    setList(list.filter(l=>l.id !== id));
  };
  return (
    <div>
      <h2>Shopping List</h2>
      <ul>
        {list.map(l=> <li key={l.id}>{l.item_id} — qty {l.quantity} <button onClick={()=>mark(l.id)}>Mark Bought</button></li>)}
      </ul>
    </div>
  )
}
