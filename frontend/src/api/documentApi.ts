const API_URL = "";

const checkstatus = (response: Response) => {
  if (response.ok) {
    return response;
  }
  // convert non-2xx HTTP Response into errors;
  const error = new Error(response.statusText);
  error.message = response;
  return Promise.reject(error);
}

export const pdftoDocxConverter = async (data: any) => {
  var formdata = new FormData()
  formdata.append("files", data.files);

  const response = await fetch(API_URL, {
    method: 'POST',
    body: formdata,
    headers: {
      "Content-Type": "multipart/form-data"
    }
  }).then(checkstatus)
  return response;
}

export const wordtoExcel = async (data: any) => {
  var formdata = new FormData()
  formdata.append("files", data.files);

  const response = await fetch(API_URL, {
    method: "POST",
    body: formdata,
    headers: {
      "Content-Type": "multipart/form-data"
    }
  }).then(checkstatus);
  return response;
}

export const docxtopdf = async (data: any) => {
  var formdata = new FormData();
  formdata.append("files", data.files);

  const response = await fetch(API_URL, {
    method: "POST",
    body: formdata,
    headers: {
      "Content-Type": "multipart/form-data"
    }
  }).then(checkstatus)
  return response;
}

export const xsxlToDocx = async (data: any) => {
  var formdata = new FormData();
  formdata.append("files", data.files);

  const response = await fetch(API_URL, {
    method: "POST",
    body: formdata,
    headers: {
      "Content-Type": "multipart/form-data"
    }
  }).then(checkstatus)
  return response;
}


export const xsxlToCorelDraw = async (data: any) => {
  var formdata = new FormData();
  formdata.append("files", data.files);

  const response = await fetch(API_URL, {
    method: "POST",
    body: formdata,
    headers: {
      "Content-Type": "multipart/form-data"
    }
  }).then(checkstatus)
  return response;
}

export const xsxlToPdf = async (data: any) => {
  var formdata = new FormData();
  formdata.append("files", data.files);

  const response = await fetch(API_URL, {
    method: "POST",
    body: formdata,
    headers: {
      "Content-Type": "multipart/form-data"
    }
  }).then(checkstatus)
  return response;
}


