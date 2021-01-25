var colors = ['green', 'blue', 'yellow', 'red']
var gameSequence = [];
var userSequence = [];
var newGame = true;
var level = 0;
var numTimesClicked = 0;


function nextSequence() {
  level++;
  $('h1').text('Level ' + level);
  var randomNumber = Math.floor(Math.random() * 4);
  var randomColor = colors[randomNumber];
  // console.log(randomColor);
  gameSequence.push(randomColor);
  playButton(randomColor);
  clickButton(randomColor);
}

function playButton(color) {
  var buttonSound = new Audio('sounds/' + color + '.mp3');
  buttonSound.play();
}

function clickButton(color) {
  var clickedButton =  $('#'+color)
  clickedButton.fadeOut(100).fadeIn(100);
  clickedButton.addClass('pressed');
  setTimeout(function () {
    clickedButton.removeClass('pressed');
  }, 100);
}

$('.btn').click(function() {

  if (newGame == true) {
    gameOver();
  } else {

  numTimesClicked++;
  var clickedButtonId = this.id;
  // console.log(clickedButtonId);
  clickButton(clickedButtonId);
  playButton(clickedButtonId);
  userSequence.push(clickedButtonId);
  checkAnswer(numTimesClicked-1);
}})

$(document).keypress(function() {
  if (newGame == true) {
    newGame = false;
    nextSequence();
  // } else {
  //   gameOver();
  // }
}})

function checkAnswer(number) {
  if (gameSequence[number] == userSequence[number]) {
    // console.log('ok')
    if (level == numTimesClicked) {
      setTimeout(function () {
        nextSequence();
      }, 1000);
      userSequence = [];
      numTimesClicked = 0; }
  } else  {
    // console.log('not ok');
    gameOver();
  }
}

function gameOver() {
  $('h1').text('Game Over. Press any key to start again...');
    var gameOverSound = new Audio('sounds/wrong.mp3');
    gameOverSound.play();
    $('body').addClass('game-over');

  setTimeout(function () {
    $('body').removeClass('game-over');
  }, 100);
  gameSequence = [];
  userSequence = [];
  newGame = true;
  level = 0;
  numTimesClicked = 0;
}
