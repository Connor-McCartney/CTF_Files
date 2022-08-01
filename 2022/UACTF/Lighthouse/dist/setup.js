var vs = Array.prototype.slice.call(document.getElementsByClassName('preset1'));
var arr = [];

arr[0] = new k1(vs[0], new Ui['P1']());
arr[2] = new k3(vs[2], new Ui['P1']())
arr[1] = new k2(vs[1], new Ui['P1']())
arr[4] = new k5(vs[4], new Ui['P1']())
arr[3] = new k4(vs[3], new Ui['P1']())
arr[6] = new k7(vs[6], new Ui['P1']())
arr[5] = new k6(vs[5], new Ui['P1']())
arr[7] = new k8(vs[7], new Ui['P1']())
function check() {
//Use this to convert the minimum number of turns to the flag
// 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
// A B C D E F G H I J K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  _  !  *
// Remember to wrap with UACTF

    g = [8, 11, 22, 4, 14, 26, 3, 21];

    for (let x in g)
        if (g[x] != arr[x].value)
            return;

    alert("dials are in the right position");
}
