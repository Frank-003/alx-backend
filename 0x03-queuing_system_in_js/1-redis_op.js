// 1-redis_op.js

import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err.message);
});

function setNewSchool(schoolName, value, callback) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(err);
      callback(err);
    } else {
      redis.print(`School ${schoolName} set to ${value}`);
      callback(null, reply);
    }
  });
}

function displaySchoolValue(schoolName, callback) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(err);
      callback(err);
    } else {
      console.log(`Value for ${schoolName}: ${reply}`);
      callback(null, reply);
    }
  });
}

// Call the functions
displaySchoolValue('Holberton', (err, value) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Initial value for Holberton: ${value}`);
  }
});

setNewSchool('HolbertonSanFrancisco', '100', (err, reply) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`setNewSchool reply: ${reply}`);
  }
});

displaySchoolValue('HolbertonSanFrancisco', (err, value) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Value for HolbertonSanFrancisco: ${value}`);
  }
});
