function hasStorage() {
  const key = 'test-db', storage = window.localStorage
  if (!storage) {
    return false
  }
  try {
    storage.setItem(key, 'a')
    storage.removeItem(key)
    return true
  } catch (e) {
    return false
  }
}

const cache = {}
const isSupported = hasStorage()

function get(key) {
  if (isSupported) {
    return localStorage[key]
  } else {
    return cache[key]
  }
}

function set(key, value) {
  if (isSupported) {
    return localStorage[key] = value
  } else {
    return cache[key] = value
  }
}

function del(key) {
  if (isSupported) {
    delete localStorage[key]
  } else {
    delete cache[key]
  }
}

export default {get, set, del}
