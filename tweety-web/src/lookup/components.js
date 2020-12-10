function lookup(method, endpoint, callback, data) {
  let jsonData; 
  if (data) {
    jsonData = JSON.stringify(data)
  }
  const xhr = new XMLHttpRequest()
  const url = `http://localhost:8000/api${endpoint}`
  const responseType = "json"
  xhr.open(method, url)
  xhr.onload = function(){
    callback(xhr.response, xhr.status)
  }
  xhr.onerror = function (e) {
    console.log(e)
    callback({"message": "The request was an error"}, 400)
  }
  xhr.send()
}

export function loadTweets(callback) {
  lookup("GET","/tweets/", callback)
  }