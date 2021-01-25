const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const https = require('https');

app.use(express.static('public'));
app.use(bodyParser.urlencoded({extended:true}));

app.get('/', function(req, res) {
  res.sendFile(__dirname + '/index.html')
});

app.post('/failure.html', function(req, res) {
  res.redirect('/');
})

app.post('/', function(req, res) {
  var first = req.body.first;
  var last = req.body.last;
  var email = req.body.email

  var data = {
    members: [
      {email_address: email,
      status: 'subscribed',
      merge_fields: {
        FNAME:first,
        LNAME:last
      }}]
  }
  var jsonData = JSON.stringify(data);
  var url='https://us7.api.mailchimp.com/3.0/lists/6b74f17bba';
  var options = {
    method: "POST",
    auth: "lui:af713e51ac75a15b459dd2dec4030409-us7"
  };
  var resp = https.request(url, options, function(response){
    response.on('data', function(data){
      // console.log(JSON.parse(data));
      // console.log(response.statusCode);

    })
    if (response.statusCode == '200') {
      res.sendFile(__dirname + '/success.html')
    } else {
      res.sendFile(__dirname + '/failure.html')
    }
  })



  resp.write(jsonData);
  resp.end();
});


app.listen(3000, function () {
  console.log('Server is up');
});




// key
// af713e51ac75a15b459dd2dec4030409-us7

// list-id
// 6b74f17bba
