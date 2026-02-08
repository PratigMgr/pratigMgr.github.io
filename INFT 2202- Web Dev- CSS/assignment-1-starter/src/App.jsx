/**
Name: Pratig Thapa Magar
Course Code: INFT 22002
Date: 2026-02-08
*/
import React, { useMemo, useEffect, useState } from 'react'
import ProductForm from './components/ProductForm'
import ProductList from './components/ProductList'
import { getAllProducts, addProduct, removeProduct } from './storage/productStorage.js';


export default function App(){
  // TODO: start with [] and consider hydrating from storage once storage helpers are implemented
  const [items, setItems] = useState([])

  // Optional: toggle between views; start on 'list'
  const [view, setView] = useState('list') // 'list' | 'form'
   // Load products from localStorage on first render
  useEffect(() => {
    setItems(getAllProducts());
  }, [])

  // TODO: compute total from items
  const total = items.length;

  function handleCreate(data){
    // TODO: validate (in the form), persist to storage, then update state
    // Example flow (do not copy/paste): create id, add to storage, reload items
    // setItems(...)
    // setView('list')
    const product = {
        ...data,
        id: items.length
          ? Math.max(...items.map(p => p.id)) + 1
          : 1,
    }
    addProduct(product)
    setItems(getAllProducts())
    setView('list')
    console.log('Create product (student to implement):', data)
  }

  function handleDelete(id){
    // TODO: remove from storage, then update state
    removeProduct(id)
    setItems(getAllProducts())
    console.log('Delete product (student to implement):', id)
  }

  return (
    <div className="container py-3">
      <header className="d-flex justify-content-between align-items-center mb-3">
        <h1 className="h3 m-0">My Web Shop</h1>
        <div className="btn-group">
          <button className={`btn btn-sm btn-${view==='list'?'primary':'outline-primary'}`} onClick={() => setView('list')}>
            Product List ({total})
          </button>
          <button className={`btn btn-sm btn-${view==='form'?'primary':'outline-primary'}`} onClick={() => setView('form')}>
            Add Product
          </button>
        </div>
      </header>

      {view === 'form' ? (
        <ProductForm onSubmit={handleCreate} />
      ) : (
        <ProductList items={items} onDelete={handleDelete} />
      )}
    </div>
  )
}
