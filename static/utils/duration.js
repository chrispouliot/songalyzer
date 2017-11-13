export const format = (durationMs) => {
  const durationFmt = {
    hours: 0,
    minutes: 0,
  }
  if (durationMs) {
    const hours = durationMs / 3600
    const decimal = hours % 1

    durationFmt.minutes = Math.floor(decimal * 60)
    durationFmt.hours = Math.floor(hours)
  }

  return durationFmt
}
