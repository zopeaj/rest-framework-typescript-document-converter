import { pdftoDocxConverter, wordtoExcel, docxtopdf, xsxlToCorelDraw, xsxlToPdf } from "../api/documentApi";


const pdftoDocxConverterService = async (data: any, errorCallback: Function, successCallback: Function, otherCallback: Function) => {
  await pdftoDocxConverter(data).then(() => {
    console.log("document converted");
    successCallback(data);
  }).catch((err) => {
    console.log(err);
    err.response.json().then((res) => {
      errorCallback(res);
    });
  }).finally(() => {
    otherCallback()
  })
}


const wordToExcelService = async (data: any, errorCallback: Function, successCallback: Function, otherCallback: Function) => {
  await wordtoExcel(data).then(() => {
    console.log("document converted");
    successCallback(data);
  }).catch((err) => {
    console.log(err);
    err.response.json().then((res) => {
      errorCallback(res);
    });
  }).finally(() => {
    otherCallback()
  })
}

const docxtoPdf = async (data: any, errorCallback: Function, successCallback: Function, otherCallback: Function) => {
  await docxtopdf(data).then(() => {
    console.log("document converted");
    successCallback();
  }).catch((err) => {
    console.log(err);
    err.response.json().then((res) => {
      errorCallback(res);
    });
  }).finally(() => {
    otherCallback();
  })
}


// addNewStudent(student).then(() => {
//   console.log("student added")
//   onClose();
//   successNotification("Student Successfully added", `${student.name} was added to the system`)
//   fetchStudents();
// }).catch((err) => {
//   console.log(err);
//   err.response.json().then((res) => {
//     errorNotification("There was an issue", `${res.message} [${res.status}] [${res.error}]`, "bottomLeft")
//   });
// }).finall(() => {
//   setSubmitting(false);
// })
// };
