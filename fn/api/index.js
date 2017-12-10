import {registerResource} from './resource'

export default {
  register: (data) => {
    return registerResource.save(data)
  },
}
