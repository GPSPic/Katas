class RecentlyUsed {
  constructor(num) {
    this.num = num;
    this.arr = [];
  }

  getArr() {
    return this.arr;
  }

  addString(str) {
    if (str === "" || str === null || str === undefined) {
    } else if (this.arr.includes(str)) {
      this.arr = this.arr.filter(s => s!== str);
      this.arr.unshift(str);
    } else if (this.arr.length < this.num && !this.arr.includes(str)) {
      this.arr.unshift(str);
    } else if (this.arr.length === this.num) {
      this.arr.pop();
      this.arr.unshift(str);
    }
  }
}

module.exports = RecentlyUsed;
