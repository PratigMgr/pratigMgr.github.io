/**
Name: Pratig Thapa Magar
Course Code: INFT 22002
Date: 2026-02-08
*/
// TODO: Implement localStorage-based persistence using JSON.parse / JSON.stringify.
// Use this key for storage:
export const STORAGE_KEY = 'a1_products';

/**
 * Safely read JSON from storage
 */
function read(key, storage) {
  try{
    const raw = storage.getItem(key);
    return raw ? JSON.parse(raw) : null;
  } catch {
    return null; // corrupted JSON or blocked storage
  }
}

function write(key, value, storage) {
  storage.setItem(key, JSON.stringify(value));
}

// TODO: return an array of products from localStorage (or [] if none)
export function getAllProducts() {
  /* your code */
  return read(STORAGE_KEY, localStorage) || [];
}

// TODO: persist a product into storage
export function addProduct(product) {
  /* push to array and persist to localStorage */
  const products = getAllProducts();
  products.push(product);
  write(STORAGE_KEY, products, localStorage);
  return products;
}

// TODO: remove a product by id and persist
export function removeProduct(id) {
  /* empty keys from localStorage */
  const a1_products = getAllProducts().filter(p => p.id !== id);
  write(STORAGE_KEY, a1_products, localStorage);
  return a1_products;
}
