const RecentlyUsed = function (num) {
    this.num = num
    this.arr = []
}

RecentlyUsed.prototype.addString = function (str) {
    if (this.arr.length < this.num && !this.arr.includes(str)) {
        this.arr.unshift(str)
    }
}

RecentlyUsed.prototype.getArr = function () {
    return this.arr
}

module.exports = RecentlyUsed