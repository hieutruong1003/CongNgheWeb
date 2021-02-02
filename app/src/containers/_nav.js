import React from 'react'
import CIcon from '@coreui/icons-react'

const _nav =  [
  {
    _tag: 'CSidebarNavItem',
    name: 'Home',
    to: '/home',
    icon: <CIcon name="cil-speedometer" customClasses="c-sidebar-nav-icon"/>,
  },
  {
    _tag: 'CSidebarNavTitle',
    _children: ['Danh Sách Table']
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Customers',
    to: '/table/customers',
    icon: '',//cil-user
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Categories',
    to: '/table/categories',
    icon: '',//cil-list-rich
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Employees',
    to: '/table/employees',
    icon: '',//cil-people
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Orders',
    to: '/table/orders',
    icon: '',//cil-restaurant-menu
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Products',
    to: '/table/products',
    icon: '',
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Shippers',
    to: '/table/shippers',
    icon: '',
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'OrderDetails',
    to: '/table/order_details',
    icon: '',
  },
  {
    _tag: 'CSidebarNavItem',
    name: 'Suppliers',
    to: '/table/suppliers',
    icon: '',
  }
]

export default _nav
