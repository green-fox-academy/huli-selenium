'use strict';

const webdriver = require('selenium-webdriver'),
  By = webdriver.By,
  until = webdriver.until;

const driver = new webdriver.Builder()
  .forBrowser('chrome')
  .build();

driver.get('http://localhost:3000');
driver.wait(check_title);
function check_title() {
  let promise = driver.getTitle().then( function(title) {
    if(title === 'HuliApp' || title === 'React App') {
      console.log('success');
      return true;
    } else {
      console.log('fail --' + title);
    }
  });
  return promise;
};

