function genScopedSlots (

el,

slots,

state

) {

// by default scoped slots are considered "stable", this allows child

// components with only scoped slots to skip forced updates from parent.

// but in some cases we have to bail-out of this optimization

// for example if the slot contains dynamic names, has v-if or v-for on them...

var needsForceUpdate = el.for || Object.keys(slots).some(function (key) {

var slot = slots[key];

return (

slot.slotTargetDynamic ||

slot.if ||

slot.for ||

containsSlotChild(slot) // is passing down slot from parent which may be dynamic

)

});

// #9534: if a component with scoped slots is inside a conditional branch,

// it's possible for the same component to be reused but with different

// compiled slot content. To avoid that, we generate a unique key based on

// the generated code of all the slot contents.

var needsKey = !!el.if;

// OR when it is inside another scoped slot or v-for (the reactivity may be

// disconnected due to the intermediate scope variable)

// #9438, #9506

// and skip force updating ones that do not actually use scope variables.

if (!needsForceUpdate) {

var parent = el.parent;

while (parent) {

if (

(parent.slotScope && parent.slotScope !== emptySlotScopeToken) ||

parent.for

) {

needsForceUpdate = true;

break

}

if (parent.if) {

needsKey = true;

}

parent = parent.parent;

}

}

var generatedSlots = Object.keys(slots)

.map(function (key) { return genScopedSlot(slots[key], state); })

.join(',');

return ("scopedSlots:_u([" + generatedSlots + "]" + (needsForceUpdate ? ",null,true" : "") + (!needsForceUpdate && needsKey ? (",null,false," + (hash(generatedSlots))) : "") + ")")

}