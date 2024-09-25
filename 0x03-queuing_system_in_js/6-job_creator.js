// 6-job_creator.js

import Queue from 'kue';

const queue = new Queue();

const jobData = {
  phoneNumber: '1234567890',
  message: 'This is a test message.',
};

queue.create('push_notification_code', jobData)
  .on('enqueue', (job) => {
    console.log('Notification job created: ', job.id);
  })
  .on('complete', (job) => {
    console.log('Notification job completed: ', job.id);
  })
  .on('failed', (job) => {
    console.log('Notification job failed: ', job.id);
  })
  .save();
