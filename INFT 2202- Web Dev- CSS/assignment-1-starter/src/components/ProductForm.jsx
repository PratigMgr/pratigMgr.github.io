import React, {useState} from 'react'
/**
Name: Pratig Thapa Magar
Course Code: INFT 22002
Date: 2026-02-08
*/
// TODO: Use useState to manage a model with fields:
// { name: '', price: '', stock: '', description: '' }
// TODO: Create a validate() that sets an errors object and returns boolean:
// - All fields required
// - price: number with up to 2 decimals, >= 0
// - stock: non-negative integer
// TODO: On submit: console.log the model; if valid, call onSubmit(normalizedData)

export default function ProductForm({ onSubmit }) {
  // const [model, setModel] = ...
  // const [errors, setErrors] = ...
  const [model, setModel] = useState({
    name: '',
    price: '',
    stock: '',
    description: '',
  });
  const [errors, setErrors] = useState({});
  const [loading, setLoading] = useState(false);

  // Step 2: Handle input change
  function handleChange(e) {
    const { name, value } = e.target;
    setModel(prev => ({...prev, [name]: value }));
  }

  // Step 3: Validation
  function validate() {
    const errs = {};

    // All fields required
    if (!model.name.trim()) errs.name = 'Name is required';
    if (!model.price.trim()) errs.price = 'Price is required';
    if (!model.stock.trim()) errs.stock = 'Stock is required';
    if (!model.description.trim()) errs.description = 'Description is required';

    // Price: number >= 0, up to 2 decimals
    if (model.price && !/^\d+(\.\d{1,2})?$/.test(model.price)) {
      errs.price = 'Price must be a number with up to 2 decimals';
    }

    // Stock: non-negative integer
    if (model.stock && !/^\d+$/.test(model.stock)) {
      errs.stock = 'Stock must be a non-negative integer';
    }

    setErrors(errs);
    return Object.keys(errs).length === 0;
  }

  async function handleSubmit(e) {
    e.preventDefault()
    console.log('FORM OK, no parent call');
    // console.log('Submitting:', model)
    // if (!validate()) return
    // onSubmit({ name: ..., price: Number(...), stock: Number(...), description: ... })
    if (!validate()) return;

    setLoading(true);

    const normalizedData = {
      name: model.name,
      price: Number(model.price),
      stock: Number(model.stock),
      description: model.description,
    };

    console.log('Submitting:', normalizedData);

    // Call parent onSubmit
    if (onSubmit) onSubmit(normalizedData);

    //Stop loading
    setLoading(false);
  }

  return (
    <form className="row g-3" onSubmit={handleSubmit} noValidate>
      <div className="col-md-6">
        <label className="form-label">Product Name</label>
        {/* TODO: Controlled input (value, onChange) and inline error */}
        <input  className="form-control" id="name" name="name" label="Name" type="text" value={model.name} onChange={handleChange} />
        {errors.name &&  <div className="text-danger">{errors.name}</div>}
      </div>

      <div className="col-md-3">
        <label className="form-label">Price</label>
        {/* TODO */}
        <input className="form-control" id="price" name="price" label="Price" type="text" value={model.price} onChange={handleChange} />
        {errors.price &&  <div className="text-danger">{errors.price}</div>}
        <div className="form-text">Format: 12.34</div>
      </div>

      <div className="col-md-3">
        <label className="form-label">Stock</label>
        {/* TODO */}
        <input className="form-control"  id="stock" name="stock" label="Stock" type="text" value={model.stock} onChange={handleChange} />
        {errors.stock &&  <div className="text-danger">{errors.stock}</div>}
      </div>

      <div className="col-12">
        <label className="form-label">Description</label>
        {/* TODO */}
        <textarea className="form-control" rows="3"id="description" name="description" label="Description" type="text" value={model.description} onChange={handleChange}></textarea>
        {errors.description &&  <div className="text-danger">{errors.description}</div>}
      </div>

      <div className="col-12 d-flex gap-2">
        <button className="btn btn-primary" type="submit">Save Product</button>
      </div>
    </form>
  )
}
