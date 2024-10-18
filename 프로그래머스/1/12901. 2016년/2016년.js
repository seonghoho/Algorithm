function solution(a, b) {
    const defaultTime = new Date('2016-01-01')
    const currentTime = new Date(`2016-${a}-${b}`) 
    const intervalDate = Math.round((currentTime - defaultTime) / (1000 * 60 * 60 * 24))
    const dDate = (intervalDate) % 7
    const daysOfWeek = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    return daysOfWeek[(dDate+5)%7]
}