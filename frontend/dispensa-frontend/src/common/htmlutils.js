export function getTitle (vm) {
    const { title } = vm.$options
    if (title) {
      return typeof title === 'function'
        ? title.call(vm)
        : title
    }
  }