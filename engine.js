// Can Math engine: the cartons a can order takes, the weeks the stock lasts, the cost a can, and the minutes the stacking takes. Exact integers, half-up on display only. No named constants; every number is the owner's own entry.
function _i(t, err, digits, lo, hi) {
  t = typeof t === "string" ? t.trim() : "";
  if (!new RegExp("^[0-9]{1," + digits + "}$").test(t)) throw new Error(err);
  var v = parseInt(t, 10);
  if (v < lo || v > hi) throw new Error(err);
  return v;
}
function _p(t, err, intDigits, places, lo, hi) {
  t = typeof t === "string" ? t.trim() : "";
  var m = new RegExp("^([0-9]{1," + intDigits + "})(?:\\.([0-9]{1," + places + "}))?$").exec(t);
  if (!m) throw new Error(err);
  var v = parseInt(m[1], 10) * Math.pow(10, places) + (m[2] ? parseInt(m[2].padEnd(places, "0"), 10) : 0);
  if (v < lo || v > hi) throw new Error(err);
  return v;
}
function _m(v) {
  var w = Math.floor(v / 100), f = String(v % 100).padStart(2, "0");
  return w + "." + f;
}
function _pl(n, one, many) { return n + (n === 1 ? one : many); }
function _v(n, one, many) { return n === 1 ? one : many; }
var _BG = "the cans must be from 1 to 1000000 with no decimal places";
var _BR = "the cans a carton must be from 1 to 1000 with no decimal places";
var _BW = "the cans a week must be from 1 to 100000 with no decimal places";
var _RL = "the cartons must be from 1 to 100000 with no decimal places";
var _PR = "the carton price must be from 0.01 to 999.99 with up to 2 decimal places";
var _BM = "the cans a minute must be from 1 to 100 with no decimal places";

function cartonsTruth(cans, perCarton) {
  var n = _i(cans, _BG, 7, 1, 1000000), b = _i(perCarton, _BR, 4, 1, 1000);
  var k = Math.floor((n + b - 1) / b), last = n - (k - 1) * b;
  return "The " + _pl(n, " can", " cans") + " at " + _pl(b, " can", " cans") + " a carton " + _v(n, "takes", "take") + " " + _pl(k, " carton", " cartons") + ", the last carton holding " + _pl(last, " can", " cans") + ".";
}
function weeksTruth(cans, weekly) {
  var n = _i(cans, _BG, 7, 1, 1000000), w = _i(weekly, _BW, 6, 1, 100000);
  var k = Math.floor(n / w), left = n - k * w;
  return "The " + _pl(n, " can", " cans") + " at " + _pl(w, " can", " cans") + " a week " + _v(n, "lasts", "last") + " " + _pl(k, " full week", " full weeks") + " with " + _pl(left, " can", " cans") + " left for the next week.";
}
function costTruth(cartons, price, cans) {
  var b = _i(cartons, _RL, 6, 1, 100000), p = _p(price, _PR, 3, 2, 1, 99999), n = _i(cans, _BG, 7, 1, 1000000);
  var cc = b * p;
  var pb = Math.floor((2 * cc + n) / (2 * n));
  return "The " + _pl(b, " carton", " cartons") + " at $" + _m(p) + " a carton " + _v(b, "comes", "come") + " to $" + _m(cc) + ", $" + _m(pb) + " a can.";
}
function timeTruth(cans, perMinute) {
  var n = _i(cans, _BG, 7, 1, 1000000), m = _i(perMinute, _BM, 3, 1, 100);
  var t = Math.floor((n + m - 1) / m), h = Math.floor(t / 60), r = t % 60;
  return "The " + _pl(n, " can", " cans") + " at " + _pl(m, " can", " cans") + " a minute " + _v(n, "takes", "take") + " " + _pl(t, " minute", " minutes") + ", " + _pl(h, " hour", " hours") + " " + _pl(r, " minute", " minutes") + ".";
}
