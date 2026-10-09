# Callbacks vs. promises vs. async/await (slides 305–307)

```sh
node callback.js     # fs.readFile with a callback
node promise.js      # fs/promises with .then/.catch
node promisify.js    # new Promise(...) by hand, and util.promisify
node async-await.js  # async/await, Promise.all, try/catch
```

To show the error path, rename `text.txt` and run them again.
