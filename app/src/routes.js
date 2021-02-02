import React from 'react'

const home = React.lazy(() => import('./views/home/Home'));
const customers = React.lazy(() => import('./views/table/customers'));
const categories = React.lazy(() => import('./views/table/categories'));
const employees = React.lazy(() => import('./views/table/employees'));
const orders = React.lazy(() => import('./views/table/orders'));
const orderdetails = React.lazy(() => import('./views/table/order_details'));
const products = React.lazy(() => import('./views/table/products'));
const shippers = React.lazy(() => import('./views/table/shippers'));
const suppliers = React.lazy(() => import('./views/table/suppliers'))




const routes = [
  { path: '/', exact: true, name: 'Home' ,component:home },
  { path: '/home', name: 'Home', component: home },
  { path: '/table', name: 'Table', component: customers, exact: true },
  { path: '/table/customers', name: 'Customers', component: customers },
  { path: '/table/categories', name: 'Categories', component: categories },
  { path: '/table/employees', name: 'Employees', component: employees},
  { path: '/table/orders', name: 'Orders', component: orders},
  { path: '/table/products', name: 'Products', component: products},
  { path: '/table/shippers', name: 'Shippers', component: shippers},
  { path: '/table/suppliers', name: 'Suppliers', component: suppliers},
  { path: '/table/order_details', name: 'OrdersDetails', component: orderdetails},
];

export default routes;


