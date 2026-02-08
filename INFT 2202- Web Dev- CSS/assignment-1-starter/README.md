
# Assignment 1 – Product Listing & Entry (Student Starter – STRICT)

This starter compiles and runs, but **core features are intentionally blank**.

## Your Tasks
- Implement **controlled form components** and **validation** in `src/components/ProductForm.jsx`.
- Implement dynamic rendering and deletion in `src/components/ProductList.jsx` + `ProductItem.jsx`.
- Implement **localStorage persistence** in `src/storage/productStorage.js` using `JSON.stringify`/`JSON.parse`.
- Wire up `App.jsx` to hydrate from storage and update state after create/delete.
- Keep everything on a **single page** (toggle provided; you may refine it).

## Run
```bash
npm install
npm run dev
```

## Hints
- Fields: `name`, `price`, `stock`, `description`.
- Validation: all required; `price` is >= 0 with up to 2 decimals; `stock` is a non-negative integer.
- Log submitted form values to the console before saving.
