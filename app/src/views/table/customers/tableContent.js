import React from "react";
import CRUD from "services/crudCustomer";

function TableContent(props) {
  var { onChangeStatus } = props;
    const { items } = props;
    var { onSelectItem } = props;

  function handleOnDelete(id) {
    CRUD.deleteOneCustomer(id).then((res) => {
      //alert("Xác nhận xóa thành công "+id);
      if (res.data.message == "Delete Customer") {
        //confirm("Xác nhận xóa Custumer có ID là: "+id +" !");
        onChangeStatus(true);
      } else {
        onChangeStatus(false);
      }
    });

  }
  function handleOnEdit(item) {
    onSelectItem(item);
  }

  return (
    <table className="table table-striped table-responsive">
      <thead>
        <tr>
          <th>ID</th>
          <th>Customer Name</th>
          <th>Contact Name</th>
          <th>Address</th>
          <th>City</th>
          <th>Postal Code</th>
          <th>Country</th>
          <th className="text-center">Delete</th>
          <th className="text-center">Edit</th>
        </tr>
      </thead>
      <tbody>
        {items.map((
          item,
          index //Map responses list data to table row
        ) => (
          <tr>
            <td scope="row">{item.CustomerID}</td>
            <td>{item.CustomerName}</td>
            <td>{item.ContactName}</td>
            <td>{item.Address}</td>
            <td>{item.City}</td>
            <td>{item.PostalCode}</td>
            <td>{item.Country}</td>
            <td className="text-center">
              <button
                className="btn btn-danger"
                onClick={(e) => { if (window.confirm('Xác nhận xóa Custumer có ID là' + item.CustomerID + "(Y/N)")) this.handleOnDelete(item.CustomerID) }}
              >
                Delete
              </button>
            </td>
            <td className="text-center">
              <button className="btn btn-primary" onClick={() => handleOnEdit(item)}>
                Edit
              </button>
            </td>
          </tr>
        ))
        }
      </tbody >
    </table >
  );
}
export default TableContent;