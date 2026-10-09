// Slide 39: EventEmitter
// Run: node event-emitter.js
import { EventEmitter } from 'node:events';

const ee = new EventEmitter();

// Subscribe: listeners run in the order they were added
ee.on('someEvent', (who) => {
  console.log(`event has occurred: ${who}`);
});

ee.once('someEvent', () => {
  console.log('this listener only runs the first time');
});

// Publish: emit() calls every listener synchronously, passing the arguments along
ee.emit('someEvent', 'Ada');
ee.emit('someEvent', 'Grace');

console.log('listeners left:', ee.listenerCount('someEvent'));
