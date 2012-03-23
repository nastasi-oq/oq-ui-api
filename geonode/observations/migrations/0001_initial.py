# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'FaultSource'
        db.create_table('observations_faultsource', (
<<<<<<< HEAD
            ('mag_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mom_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mag_pref', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mag_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dis_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mom_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
=======
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fault', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['observations.Fault'])),
            ('fault_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('source_nm', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('length_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
>>>>>>> master
            ('length_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('contrib', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('slip_typ', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mov_max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('u_sm_d_pre', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mov_pref', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dip_pref', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('length_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('u_sm_d_com', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dip_min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PolygonField')(dim=3)),
            ('dip_dir', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('all_com', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dis_pref', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('aseis_com', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dip_max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('slip_r_com', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('fault_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('low_d_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('low_d_pref', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dip_com', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('aseis_slip', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('slip_com', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('area_pref', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('width_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('u_sm_d_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('re_int_min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('re_int_max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('re_int_pre', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('compiler', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
<<<<<<< HEAD
            ('length_pre', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('width_pref', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('width_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('fault', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['observations.Fault'])),
            ('area_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mom_pref', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dis_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('low_d_com', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('slip_r_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('u_sm_d_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('area_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('slip_r_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('low_d_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mov_min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('slip_r_pre', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
=======
            ('contrib', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PolygonField')(dim=3)),
            ('created', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
>>>>>>> master
        ))
        db.send_create_signal('observations', ['FaultSource'])

        # Adding model 'Fault'
        db.create_table('observations_fault', (
            ('dis_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('length_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('contrib', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('slip_typ', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mov_max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('u_sm_d_pre', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mov_pref', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dip_min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('length_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('u_sm_d_com', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dip_pref', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dip_dir', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('all_com', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dis_pref', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('aseis_com', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dip_max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('slip_r_com', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('fault_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('low_d_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('low_d_pref', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dip_com', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('down_thro', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('aseis_slip', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('slip_com', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('strike', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('re_int_max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('u_sm_d_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('episodi_is', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('re_int_min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('re_int_pre', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('compiler', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
<<<<<<< HEAD
            ('length_pre', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('episodi_ac', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('dis_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('low_d_com', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('slip_r_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('u_sm_d_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mov_min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('slip_r_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('low_d_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('slip_r_pre', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
=======
            ('contrib', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
>>>>>>> master
            ('simple_geom', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')(null=True, blank=True)),
        ))
        db.send_create_signal('observations', ['Fault'])

        # Adding model 'FaultSection'
        db.create_table('observations_faultsection', (
            ('dis_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('length_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('contrib', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mov_max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('u_sm_d_pre', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mov_pref', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sec_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('length_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('u_sm_d_com', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dip_pref', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dip_dir', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('all_com', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dis_pref', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('aseis_com', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dip_max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('slip_r_com', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('slip_typ', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('low_d_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('low_d_pref', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dip_com', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('down_thro', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('aseis_slip', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('slip_com', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('strike', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('re_int_max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('u_sm_d_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('episodi_is', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('re_int_min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('re_int_pre', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('compiler', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
<<<<<<< HEAD
            ('length_pre', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('episodi_ac', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('dis_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('low_d_com', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dip_min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('slip_r_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('u_sm_d_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('mov_min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('slip_r_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('low_d_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('slip_r_pre', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
=======
            ('contrib', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
>>>>>>> master
        ))
        db.send_create_signal('observations', ['FaultSection'])

        # Adding M2M table for field fault on 'FaultSection'
        db.create_table('observations_faultsection_fault', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('faultsection', models.ForeignKey(orm['observations.faultsection'], null=False)),
            ('fault', models.ForeignKey(orm['observations.fault'], null=False))
        ))
        db.create_unique('observations_faultsection_fault', ['faultsection_id', 'fault_id'])

        # Adding model 'Trace'
        db.create_table('observations_trace', (
            ('scale', self.gf('django.db.models.fields.BigIntegerField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('loc_meth', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accuracy', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal('observations', ['Trace'])

        # Adding M2M table for field fault_section on 'Trace'
        db.create_table('observations_trace_fault_section', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('trace', models.ForeignKey(orm['observations.trace'], null=False)),
            ('faultsection', models.ForeignKey(orm['observations.faultsection'], null=False))
        ))
        db.create_unique('observations_trace_fault_section', ['trace_id', 'faultsection_id'])

        # Adding model 'SiteObservation'
        db.create_table('observations_siteobservation', (
            ('scale', self.gf('django.db.models.fields.BigIntegerField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('s_feature', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accuracy', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal('observations', ['SiteObservation'])

        # Adding M2M table for field fault_section on 'SiteObservation'
        db.create_table('observations_siteobservation_fault_section', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('siteobservation', models.ForeignKey(orm['observations.siteobservation'], null=False)),
            ('faultsection', models.ForeignKey(orm['observations.faultsection'], null=False))
        ))
        db.create_unique('observations_siteobservation_fault_section', ['siteobservation_id', 'faultsection_id'])

        # Adding model 'Observations'
        db.create_table('observations_observations', (
            ('net_slip_rate_pref', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('site', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('vertical_slip_rate_pref', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('slip_rate_category', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('observationType', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('vertical_slip_rate_min', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('slipType', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('vertical_slip_rate_max', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('net_slip_rate_max', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('dip_slip_rate_min', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('summary_id', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('dip_slip_rate_pref', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('net_slip_rate_min', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('rake', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('strike_slip_rate_min', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('hv_ratio', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('dip_slip_rate_max', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('strike_slip_rate_pref', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('marker_age', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('strike_slip_rate_max', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('observations', ['Observations'])

        # Adding model 'Fold'
        db.create_table('observations_fold', (
            ('symmetry', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('fold_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('simple_fold_geom', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')(null=True, blank=True)),
            ('dip_dir', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('length_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('contrib', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('u_sm_d_pre', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('asymm_dir', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('dip_min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('length_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('u_sm_d_com', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dip_pref', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('strike', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('all_com', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dip_max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('slip_r_com', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('slip_typ', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('low_d_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('low_d_pref', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dip_com', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('aseis_slip', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('slip_com', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fold_type', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('re_int_max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('u_sm_d_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('episodi_is', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('re_int_min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('re_int_pre', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('compiler', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('length_pre', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=3, blank=True)),
            ('episodi_ac', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('low_d_com', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('slip_r_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('u_sm_d_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('slip_r_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('low_d_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('slip_r_pre', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('observations', ['Fold'])

        # Adding model 'FoldSection'
        db.create_table('observations_foldsection', (
            ('asymm_dir', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('dip_limbs', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('length_max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('contrib', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('tilt_rate', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('surf_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dip_axial', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('symmetry', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('mov_pref', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sec_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('length_min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plunge', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fold_type', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('mov_min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('episodi_is', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('mov_max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('compiler', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('length_pre', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=3, blank=True)),
            ('growth_vert', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('growth_hori', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('episodi_ac', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('all_com', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('observations', ['FoldSection'])

        # Adding M2M table for field fold on 'FoldSection'
        db.create_table('observations_foldsection_fold', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('foldsection', models.ForeignKey(orm['observations.foldsection'], null=False)),
            ('fold', models.ForeignKey(orm['observations.fold'], null=False))
        ))
        db.create_unique('observations_foldsection_fold', ['foldsection_id', 'fold_id'])

        # Adding model 'FoldTrace'
        db.create_table('observations_foldtrace', (
            ('scale', self.gf('django.db.models.fields.BigIntegerField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('loc_meth', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')()),
            ('tid', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accuracy', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal('observations', ['FoldTrace'])

        # Adding M2M table for field fold_section on 'FoldTrace'
        db.create_table('observations_foldtrace_fold_section', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('foldtrace', models.ForeignKey(orm['observations.foldtrace'], null=False)),
            ('foldsection', models.ForeignKey(orm['observations.foldsection'], null=False))
        ))
        db.create_unique('observations_foldtrace_fold_section', ['foldtrace_id', 'foldsection_id'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'FaultSource'
        db.delete_table('observations_faultsource')

        # Deleting model 'Fault'
        db.delete_table('observations_fault')

        # Deleting model 'FaultSection'
        db.delete_table('observations_faultsection')

        # Removing M2M table for field fault on 'FaultSection'
        db.delete_table('observations_faultsection_fault')

        # Deleting model 'Trace'
        db.delete_table('observations_trace')

        # Removing M2M table for field fault_section on 'Trace'
        db.delete_table('observations_trace_fault_section')

        # Deleting model 'SiteObservation'
        db.delete_table('observations_siteobservation')

        # Removing M2M table for field fault_section on 'SiteObservation'
        db.delete_table('observations_siteobservation_fault_section')

        # Deleting model 'Observations'
        db.delete_table('observations_observations')

        # Deleting model 'Fold'
        db.delete_table('observations_fold')

        # Deleting model 'FoldSection'
        db.delete_table('observations_foldsection')

        # Removing M2M table for field fold on 'FoldSection'
        db.delete_table('observations_foldsection_fold')

        # Deleting model 'FoldTrace'
        db.delete_table('observations_foldtrace')

        # Removing M2M table for field fold_section on 'FoldTrace'
        db.delete_table('observations_foldtrace_fold_section')
    
    
    models = {
        'observations.fault': {
            'Meta': {'object_name': 'Fault'},
            'all_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'compiler': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'contrib': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dis_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'down_thro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'episodi_ac': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'episodi_is': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'fault_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_pre': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'simple_geom': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'null': 'True', 'blank': 'True'}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_typ': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'strike': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'observations.faultsection': {
            'Meta': {'object_name': 'FaultSection'},
            'all_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'compiler': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'contrib': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dis_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'down_thro': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'episodi_ac': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'episodi_is': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'fault': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['observations.Fault']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_pre': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sec_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_typ': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'strike': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'observations.faultsource': {
            'Meta': {'object_name': 'FaultSource'},
            'all_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'area_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'area_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'area_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'compiler': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'contrib': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'created': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dis_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dis_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fault': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['observations.Fault']"}),
            'fault_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'geom': ('django.contrib.gis.db.models.fields.PolygonField', [], {'dim': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mag_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mag_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mag_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mom_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mom_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mom_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_pre': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_typ': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'width_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'width_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'width_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'observations.fold': {
            'Meta': {'object_name': 'Fold'},
            'all_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'aseis_slip': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'asymm_dir': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'compiler': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'contrib': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '3', 'blank': 'True'}),
            'dip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_dir': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'episodi_ac': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'episodi_is': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'fold_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fold_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'low_d_pref': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            're_int_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            're_int_pre': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'simple_fold_geom': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'null': 'True', 'blank': 'True'}),
            'slip_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_r_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slip_typ': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'strike': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'symmetry': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'u_sm_d_com': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'u_sm_d_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'observations.foldsection': {
            'Meta': {'object_name': 'FoldSection'},
            'all_com': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'asymm_dir': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'compiler': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'contrib': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '3', 'blank': 'True'}),
            'dip_axial': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dip_limbs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'episodi_ac': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'episodi_is': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'fold': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['observations.Fold']", 'symmetrical': 'False'}),
            'fold_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'growth_hori': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'growth_vert': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length_max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_pre': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mov_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_min': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mov_pref': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'plunge': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sec_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'surf_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'symmetry': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'tilt_rate': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'observations.foldtrace': {
            'Meta': {'object_name': 'FoldTrace'},
            'accuracy': ('django.db.models.fields.BigIntegerField', [], {}),
            'fold_section': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['observations.FoldSection']", 'symmetrical': 'False'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loc_meth': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'scale': ('django.db.models.fields.BigIntegerField', [], {}),
            'tid': ('django.db.models.fields.IntegerField', [], {})
        },
        'observations.observations': {
            'Meta': {'object_name': 'Observations'},
            'dip_slip_rate_max': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'dip_slip_rate_min': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'dip_slip_rate_pref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'hv_ratio': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marker_age': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'net_slip_rate_max': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'net_slip_rate_min': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'net_slip_rate_pref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'observationType': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'rake': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slipType': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'slip_rate_category': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'strike_slip_rate_max': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'strike_slip_rate_min': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'strike_slip_rate_pref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'summary_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'vertical_slip_rate_max': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'vertical_slip_rate_min': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'vertical_slip_rate_pref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'observations.siteobservation': {
            'Meta': {'object_name': 'SiteObservation'},
            'accuracy': ('django.db.models.fields.BigIntegerField', [], {}),
            'fault_section': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['observations.FaultSection']", 'symmetrical': 'False'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            's_feature': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'scale': ('django.db.models.fields.BigIntegerField', [], {})
        },
        'observations.trace': {
            'Meta': {'object_name': 'Trace'},
            'accuracy': ('django.db.models.fields.BigIntegerField', [], {}),
            'fault_section': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['observations.FaultSection']", 'symmetrical': 'False'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loc_meth': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'scale': ('django.db.models.fields.BigIntegerField', [], {})
        }
    }
    
    complete_apps = ['observations']

