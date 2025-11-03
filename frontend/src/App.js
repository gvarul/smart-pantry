import React from "react";
import { Routes, Route, Link } from "react-router-dom";
import Inventory from "./pages/Inventory";
import AddItem from "./pages/AddItem";
import UseItem from "./pages/UseItem";
import ShoppingList from "./pages/ShoppingList";

function App(){
  return (
    <div style={{padding:20}}>
      <h1>Smart Pantry</h1>
      <nav>
        <Link to="/">Inventory</Link> | <Link to="/add">Add Item</Link> | <Link to="/use">Use Item</Link> | <Link to="/shopping">Shopping</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Inventory />} />
        <Route path="/add" element={<AddItem />} />
        <Route path="/use" element={<UseItem />} />
        <Route path="/shopping" element={<ShoppingList />} />
      </Routes>
    </div>
  );
}

export default App;
