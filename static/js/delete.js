function deleteGender(endPoint,genderId){

  console.log(endPoint, genderId);
  fetch("/delete/"+endPoint+"/"+genderId,{
    method: "POST",
    body: JSON.stringify({
      endPoint : endPoint,
      genderId : genderId
    }),
  }).then((_res) => {
    window.location.href = "/";
  })
}