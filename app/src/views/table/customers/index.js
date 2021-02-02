import CRUD from "services/crudCustomer";
import React from 'react'
import TableContent from "./tableContent";
import FormInput from "./formInput"


const Customer = () => {
  const [listCustomers, setListCustomers] = React.useState([]); //Create listCustomers State
  const [status, setStatus] = React.useState(false);
  const [selectItem, setSelectItem] = React.useState(null);

  const RetrieveAllCustomers = () => {
    // <=> function RetrieveAllCustomers(){}
    console.log("Retrieve all customer");
    CRUD.getCustomerAll().then((res) => {
      //console.log(res);
      setListCustomers(res.data); //Set list customers after get all result from server
      //console.log(res.data)
      //console.log(listCustomers);
    });
  };
  const onSelectItem = (item) => {
    setSelectItem(item);
  }
  const onChangeStatus = (status) => {
    setStatus(status);
}
  React.useEffect(() => {
    RetrieveAllCustomers();
  }, [status]);
  return (
    <div class="container-fuil">
      <div className="row">
        <div className="col col-sm-9">
          <TableContent
            items={listCustomers}
            onChangeStatus={onChangeStatus}
            onSelectItem={onSelectItem}
          />
        </div>
        <div className="col col-sm-3">
          <FormInput onSelectItem = {onSelectItem} selectItem = {selectItem} onChangeStatus={onChangeStatus} />
        </div>

      </div>
    </div>
  )
}

export default Customer
