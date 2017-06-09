/**
 * @copyright	Copyright (c) 2013 Skyline (http://extstore.com). All rights reserved.
 * @license		GNU General Public License version 2 or later; see LICENSE.txt
 */

function SL_SFMegaMenu(id, containerClass) {
	var hasClass	= function(el, className) {
		var classNames	= el.className.replace('  ', '').trim().split(' ');

		if (classNames.indexOf(className) == -1) {
			return false;
		} else {
			return true;
		}
	}


	var els			= document.getElementById(id).getElementsByTagName('li');
	var container	= null;

	if (containerClass) {
		container	= document.getElementById(id).parentNode;

		while (!hasClass(container, containerClass) && container.parentNode && container.tagName != 'HTML') {
			container	= container.parentNode;
		}

		if (!hasClass(container, containerClass)) {
			container = null;
		}
	}


	var mouseOver	= function() {
		if (!hasClass(this, 'haschild-over')) {
			this.className += ' haschild-over';

			if (container) {
				var child			= this.children[1];
				var childRect		= child.getBoundingClientRect();
				var containerRect	= container.getBoundingClientRect();
				var parentRect		= this.getBoundingClientRect();

				if (childRect.width < containerRect.width) {
					if (childRect.right > containerRect.right) {
						child.style.left	= (parseFloat(window.getComputedStyle(child).left) + containerRect.right - childRect.right) + 'px';
					} else {

					}
				} else {
					child.style.left		= (parseFloat(window.getComputedStyle(container).left) - parseFloat(window.getComputedStyle(child).left)) + 'px';
				}
			}
		}
	}

	var mouseOut	= function() {
		this.className	= this.className.replace(new RegExp(" haschild-over\\b"), "");
	}

	for (var i = 0; i < els.length; i++) {
		var el	= els[i];

		if (hasClass(el, 'haschild')) {
			if (el.addEventListener) {
				el.addEventListener('mouseover', mouseOver, false);
				el.addEventListener('mouseout', mouseOut, false);
			} else if (el.attachEvent) {
				el.attachEvent('onmouseover', mouseOver);
				el.attachEvent('onmouseout', mouseOut);
			} else {
				el.onmouseover	= mouseOver;
				el.onmouseout	= mouseOut;
			}
		}
	}

	function menuTouch(event) {
		var i;
		var len = els.length;
		var noclick = !(this.dataNoclick);

		for (i = 0; i < len; i++) {
			var el = els[i];

			if (hasClass(el, 'haschild')) {
				el.dataNoclick = false;
			}
		}

		this.dataNoclick = noclick;
		this.focus();
	}

	function menuClick(event) {
		if (this.dataNoclick) {
			event.preventDefault();
		}
	}
}