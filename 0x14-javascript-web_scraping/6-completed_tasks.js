#!/usr/bin/node

const request = require("request");
const url = 'https://jsonplaceholder.typicode.com/todos';
request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
        const tasks = JSON.parse(body);
        const completedTasks = tasks.filter(task => task.completed === true);
        const users = {};
        completedTasks.forEach(task => {
            if (users[task.userId]) {
                users[task.userId]++;
            } else {
                users[task.userId] = 1;
            }
        });
        Object.keys(users).forEach(userId => {
            console.log(`User ${userId} completed ${users[userId]} tasks.`);
        });
    } else {
        console.log(`Error requesting API: ${error}`);
    }
});
