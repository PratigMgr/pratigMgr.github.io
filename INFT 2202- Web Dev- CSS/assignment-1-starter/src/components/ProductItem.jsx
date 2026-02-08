/**
Name: Pratig Thapa Magar
Course Code: INFT 22002
Date: 2026-02-08
*/
import React from 'react'

export default function ProductItem({ product, onDelete }){
  // TODO: render a Bootstrap card with product details and a Delete button
  if (!product) return null;
  return (
    <div className="col-md-4 mb-3">
      <div className="card h-100">
        <div className="card-body d-flex flex-column">
          <h5 className="card-title">{product.name}</h5>

          <p className="card-text">{product.description}</p>

          <p className="card-text">
            <strong>Price:</strong> ${product.price}
          </p>

          <p className="card-text">
            <strong>Stock:</strong> {product.stock}
          </p>

          <button
            className="btn btn-danger mt-auto"
            onClick={() => onDelete(product.id)}
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  );
}