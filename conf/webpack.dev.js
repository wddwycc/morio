const {EnvironmentPlugin} = require('webpack')
const config = require('./webpack.base')

config.devServer = {
  port: 8088,
  host: '127.0.0.1',
  headers: {
    'Access-Control-Allow-Origin': '*'
  },
  proxy: {
    "/api": "http://localhost:5000"
  }
}

config.plugins = config.plugins.concat(
  new EnvironmentPlugin({
    NODE_ENV: 'development'
  })
)

module.exports = config
