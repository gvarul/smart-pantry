import React, {useState} from "react";
import { api } from "../api";
import BarcodeScanner from "../components/BarcodeScanner";

export default function AddItem(){
  const [form, setForm] = useState({name:"", quantity:1, unit:"pcs", barcode:"", user_id:1, expiry_date:""});
  const [scanning, setScanning] = useState(false);

  const submit = async () => {
    try{
      await api.post("/items/", form);
      alert("Added");
    } catch(e){ console.error(e); alert("Error"); }
  };

  return (
    <div>
      <h2>Add Item</h2>
      <label>Name: <input value={form.name} onChange={e=>setForm({...form,name:e.target.value})} /></label><br/>
      <label>Qty: <input type="number" value={form.quantity} onChange={e=>setForm({...form,quantity:parseFloat(e.target.value)})} /></label><br/>
      <label>Unit: <input value={form.unit} onChange={e=>setForm({...form,unit:e.target.value})} /></label><br/>
      <label>Expiry: <input type="date" onChange={e=>setForm({...form,expiry_date:e.target.value})} /></label><br/>
      <label>Barcode: <input value={form.barcode} onChange={e=>setForm({...form,barcode:e.target.value})} /></label><br/>
      <button onClick={()=>setScanning(!scanning)}>Toggle Scan</button>
      {scanning && <BarcodeScanner onDetected={(code)=>{setForm({...form,barcode:code}); setScanning(false);}} />}
      <br/>
      <button onClick={submit}>Add</button>
    </div>
  )
}
