/**
Name: Pratig Thapa Magar
Course Code: INFT 22002
Date: 2026-02-08
*/
import React from 'react'
import ProductItem from './ProductItem'

export default function ProductList({ items, onDelete }) {
  // if items is empty, show "No products available."
  if (items.length === 0) {
    return (
      <div>
        <h2 className="h5 mb-3">Products</h2>
        <div className="alert alert-secondary">No products available.</div>
      </div>
    );
  } else {
    // otherwise, map items to <ProductItem />
    return (
      <div>
        <h2 className="h5 mb-3">Products</h2>
        <div className="row">
          {items.map((product) => (
            <ProductItem key={product.id} product={product} onDelete={onDelete} />
          ))}
        </div>
      </div>
    );
  }
}

