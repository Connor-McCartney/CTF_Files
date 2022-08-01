var k3;
k3 = function(input, ui) {
    var container = document.createElement('div');
    container.setAttribute('tabindex', 0);
    input.parentNode.replaceChild(container, input);
    input.style.cssText = 'position: absolute; top: -10000px';
    input.setAttribute('tabindex', -1);
    container.appendChild(input);

    var settings = this.settings = this._getSettings(input);


    this.value = input.value = 4;
    this.input = input;
    this.min = settings.min;

    this.ui = ui;

    var events = {
        //   keydown: this._handleKeyEvents.bind(this),
        //    mousewheel: this._handleWheelEvents.bind(this),
        //  DOMMouseScroll: this._handleWheelEvents.bind(this),
        // touchstart: this._handleMove.bind(this, 'touchmove', 'touchend'),
        mousedown: this._handleMove.bind(this, 'mouseup')
    };

    for (var event in events) {
        container.addEventListener(event, events[event], false);
    }

    //container.style.cssText = 'position: relative; width:' + settings.width + 'px;' + 'height:' + settings.height + 'px;';
    //    container.style.cssText = 'position: relative; width:' + settings.width/1.8 + 'px;' + 'height:' + settings.height + 'px;';
    container.style.cssText = 'margin: auto; width:' + settings.width / 1.8 + 'px;' + 'height:' + settings.height / 1.5 + 'px;';
    //container.style.cssText = 'margin: auto; width:' + settings.width/1.8 + 'px;' + 'height:' + settings.height + 'px;';

    ui.init(container, settings);
    this.container = container;
    this.changed(0);

};

k3.prototype = {

    _handleMove: function(onMove, onEnd) {
        arr[0].changed(48);
        arr[1].changed(30);
        arr[2].changed(1);
        arr[3].changed(47);
        arr[4].changed(46);
        arr[5].changed(27);
        arr[6].changed(20);
        arr[7].changed(25);
    },

    _updateWhileMoving: function(event) {
        event.preventDefault();
        var e = event.changedTouches ? event.changedTouches[0] : event;
        var x = this.centerX - e.pageX;
        var y = this.centerY - e.pageY;
        var deg = Math.atan2(-y, -x) * 180 / Math.PI + 90 - this.settings.angleoffset;
        var percent;

        if (deg < 0) {
            deg += 360;
        }
        deg = deg % 360;
        if (deg <= this.settings.anglerange) {
            percent = Math.max(Math.min(1, deg / this.settings.anglerange), 0);
        } else {
            percent = +(deg - this.settings.anglerange < (360 - this.settings.anglerange) / 2);
        }
        var range = this.settings.range;
        var value = this.min + range * percent;

        var step = (this.settings.max - this.min) / range;
        this.value = this.input.value = Math.round(value / step) * step;
        this.ui.update(percent, this.value);
        this.triggerChange();
    },

    changed: function(direction) {
        this.input.value = this.limit(parseFloat(this.input.value) + direction * (this.input.step || 1));
        this.value = this.input.value;
        this.ui.update(this._valueToPercent(), this.value);
        this.triggerChange();
    },

    changedNoTrigger: function(direction) {
        this.input.value = this.limit(parseFloat(this.input.value) + direction * (this.input.step || 1));
        this.value = this.input.value;
        this.ui.update(this._valueToPercent(), this.value);
    },


    updateNoTrigger: function(value) {
        this.input.value = this.limit(value);
        this.value = this.input.value;
        this.ui.update(this._valueToPercent(), this.value);
    },


    update: function(value) {
        this.input.value = this.limit(value);
        this.value = this.input.value;
        this.ui.update(this._valueToPercent(), this.value);
        this.triggerChange();
    },

    triggerChange: function() {
        if (document.createEventObject) {
            var evt = document.createEventObject();
            this.input.fireEvent("onchange", evt);
        } else {
            this.input.dispatchEvent(new Event('change'));
        }
    },

    _valueToPercent: function() {
        return this.value != null ? 100 / this.settings.range * (this.value - this.min) / 100 : this.min;
    },

    limit: function(value) {
        return value % 29;
    },

    _getSettings: function(input) {
        var labels;

        if (input.dataset.labels) {
            labels = input.dataset.labels.split(',');
        }
        var settings = {
            max: labels ? labels.length - 1 : parseFloat(input.max),
            min: labels ? 0 : parseFloat(input.min),
            step: parseFloat(input.step) || 1,
            angleoffset: 0,
            anglerange: 360,
            labels: labels
        };
        settings.range = settings.max - settings.min;
        var data = input.dataset;
        for (var i in data) {
            if (data.hasOwnProperty(i) && i !== 'labels') {
                var value = +data[i];
                settings[i] = isNaN(value) ? data[i] : value;
            }
        }
        return settings;
    }
};

