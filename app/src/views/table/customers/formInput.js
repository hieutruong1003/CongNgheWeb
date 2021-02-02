import React, { useEffect } from "react";
import CRUD from "services/crudCustomer";

function FormInput(props) {

  var { onChangeStatus } = props;
  const { onSelectItem } = props;
  const { selectItem } = props;
  const [status, setStatus] = React.useState(false);
  // onSubmitSuccess => onUpdateSuccess
  // Syntax js, defind {abc: "text", def: 12} => object (properties: abc, def)
  const [postData, setPostData] = React.useState({
    //Create postData state
    customerName: "",
    contactName: "",
    address: "",
    city: "",
    postalCode: "",
    country: "",
  });
  const data = {
    customerName: "",
    contactName: "",
    address: "",
    city: "",
    postalCode: "",
    country: ""
  }

  function handleChangeData(e) {
    e.preventDefault();
    setPostData({ ...postData, [e.target.name]: e.target.value }); //Only change customer name in postData
  }
  const notifyData = () => {
    setStatus(false);
    if (selectItem === null) {

    } else {
      setPostData(selectItem);
      document.getElementById('btnAdd').textContent = 'Edit';
    }
  }


  useEffect(() => {
    notifyData();
  }, [status, selectItem])

  function handleOnClickSubmit(e) {
    // Handle event when click submit button
    e.preventDefault();
    console.log("POST DATA: " + postData);
    if (selectItem === null) {
      CRUD.createOneCustomer(postData).then((res) => {
        if (res.data.message === "Insert Success!") {
          alert(res.data.message);
          onChangeStatus(true);
          setPostData(data);
          setStatus(true);
        } else {
          alert("Insert Fail !");
        }

      }).catch((err) => {
        alert(err);
      });
    } else {
      CRUD.updateOneCustomer(postData).then(res => {
        if (res.data.message === "Update Success !") {
          alert(res.data.message);
          onChangeStatus(true);
          document.getElementById('btnAdd').textContent = 'Submit';
          onSelectItem(null);
          setPostData(data);
          setStatus(true);
        } else {
          alert("Update Fail !");
        }

      });

    }
  }
  function handleOnClickCancel() {
    document.getElementById("_customerName").value = "";
    document.getElementById("_contactName").value = "";
    document.getElementById("_address").value = "";
    document.getElementById("_city").value = "";
    document.getElementById("_postalCode").value = "";
    document.getElementById("_country").value = "";
  }

  function handleOnSubmit(e) {
    e.preventDefault(); // prevent reload page if submit
  }

  return (
    <form onSubmit={handleOnSubmit}>
      <h3 >Form insert Customer</h3>
      <div class="form-group">
        <label for="_customerName">Customer Name</label>
        <input
          class="form-control"
          type="text"
          name="customerName"
          value={postData?.customerName}
          onChange={handleChangeData}
          placeholder="Customer Name"
          id="_customerName"
        />
      </div>
      <div class="form-group">
        <label for="_contactName">Contact Name</label>
        <input
          className="form-control"
          type="text"
          name="contactName"
          value={postData?.contactName}
          onChange={handleChangeData}
          placeholder="Contact Name"
          id="_contactName"
        />
      </div>
      <div class="form-group">
        <label for="_address">Address</label>
        <input
          className="form-control"
          type="text"
          name="address"
          value={postData?.address}
          onChange={handleChangeData}
          placeholder="Address"
          id="_address"
        />
      </div>
      <div class="form-group">
        <label for="_city">City</label>
        <input
          className="form-control"
          type="text"
          name="city"
          value={postData?.City}
          onChange={handleChangeData}
          placeholder="City"
          id="_city"
        />
      </div>
      <div class="form-group">
        <label for="_postalCode">Postal Code</label>
        <input
          className="form-control"
          type="text"
          name="postalCode"
          value={postData?.postalCode}
          onChange={handleChangeData}
          placeholder="Postal Code"
          id="_postalCode"
        />
      </div>
      <div class="form-group">
        <label for="_country">country</label>
        <input
          className="form-control"
          type="text"
          name="country"
          value={postData?.country}
          onChange={handleChangeData}
          placeholder="Country"
          id="_country"
        />
      </div>

      <div className="text-center ">
        <button
          className="btn btn-facebook mx-1"
          name="btnSubmit"
          value="submit"
          onClick={handleOnClickSubmit}
          color="primary"
          id="btnAdd"
        >
          Add{" "}
        </button>
        <button
          className="btn btn-danger mx-1"
          name="btnCancle"
          value="cancel"
          onClick={handleOnClickCancel}
          color="primary"
        >
          Cancel{" "}
        </button>
      </div>
    </form>
  );
}
export default FormInput;
