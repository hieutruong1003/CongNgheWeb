import HttpRequest from "./http-common";

const getCustomerAll = async () => {
  return await HttpRequest.get("http://localhost:8080/customer/all");
};

const createOneCustomer = (data) => {
  return HttpRequest.post("http://localhost:8080/customer/insert", data);
};

const deleteOneCustomer = (id) => {
  return HttpRequest.delete(`http://localhost:8080/customer/delete/${id}`);
};

const updateOneCustomer = (id, data) => {
  return HttpRequest.put(`http://localhost:8080/customer/update/${id}`, data);
};

export default { getCustomerAll, createOneCustomer, deleteOneCustomer, updateOneCustomer };
